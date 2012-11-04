# coding: utf-8
import logging
import csv, codecs, cStringIO

logging.basicConfig(format="%(levelname)s: %(msg)s")

class Table:
    def __init__(self, path, **kwargs):
        # override the default options
        csv_opts, has_header, how_deep = self._get_opts(kwargs)

        # read the csv file and clean the data
        rows = list(UnicodeReader(open(path), **csv_opts))
        # where the data start
        start = 1 if has_header else 0
        # how deep to discover the data types (0 = all the column)
        end = (how_deep or len(rows)) + start

        # initialize the table
        self.header = [ 
            {
                u'index': i,
                u'slug' : self._slugify(head) if has_header else u'c%s' % i,
                u'name' : head if has_header else u'Column %s' % i,
                u'type' : self._discover([r[i] for r in rows[start:end]], i)
            } 
            for i, head in enumerate(rows[0])
        ]
        self.data = self._parse(rows[start:])
            
        self.rows_count = len(self.data)
        self.cols_count = len(self.header)


    def value(self, row, column, as_dict=False):
        col_num = self._get_header_for(column)['index']
        value   = self.row(row)[col_num]

        return self._make_dict(value, col_num) if as_dict else value

    def row(self, index, as_dict=False):
        if as_dict:
            return [self._make_dict(v, h) for h, v in enumerate(self.data[index])]
        else:
            return self.data[index]

    def rows(self, as_dict=False):
        if as_dict:
            return [self.row(i, as_dict) for i in range(self.rows_count)]
        else:
            return self.data

    def column(self, column, as_dict=False):
        head = self._get_header_for(column)
        if as_dict:
          head['values'] = [row[head['index']] for row in self.rows()]
          return head
        else:
          return [row[head['index']] for row in self.rows()]

    def columns(self, as_dict=False):
        return [self.column(i, as_dict) for i in range(self.cols_count)]

    def _make_dict(self, value, column):
        result = self._get_header_for(column)
        result[u'value'] = value

        return result

    def _get_header_for(self, column):
        if type(column) in [str, unicode]:
            return dict([e for e in self.header if e['slug'] == self._slugify(column)].pop())
        else:
            return dict(self.header[int(column)])
        
    def _get_opts(self, opts):
        csv_opts = {
            'delimiter': opts.get('delimiter', ';'),
            'quotechar': opts.get('quotechar', '"')
        }
        has_header = opts.get('header', True)
        how_deep   = opts.get('how_deep', 0)
        
        return (csv_opts, has_header, how_deep)

    def _discover(self, column, col_number):
        types = [int, float, unicode]

        for cast in types:
            if cast is unicode:
                # don't iterate - there are no other options left
                break

            empty_cells = 0
            for cell in column:
                # skip empty cells, but keep track of them
                if not cell.strip():
                    empty_cells += 1
                    continue
                
                try:
                    cast(cell)
                except:
                    break
            # if run to the end of cells... 
            else:
                # ...break types iteration
                break

        if empty_cells:
          logging.warning("Some empty cells found in column %d" % col_number)

        # return the last successful type
        return cast if empty_cells != len(column) else unicode

    def _parse(self, data):
        def __parse(cell, head):
            col_type = head['type']

            if col_type is unicode:
                cell = cell.strip()

            return col_type(cell) if cell else None

        return [[__parse(c, h) for c, h in zip(row, self.header)] for row in data]

    def _slugify(self, text):
        import re
        non_alpha = re.compile(r'\W+')
        chars = { 
            u'ą': u'a', u'ż': u'z', u'ś': u's',
            u'ź': u'z', u'ę': u'e', u'ć': u'c',
            u'ń': u'n', u'ó': u'o', u'ł': u'l'
        }

        if type(text) is str:
          text = text.decode('utf-8')
        else:
          text = unicode(text)

        text = text.lower()
        for k, v in chars.items():
            text = text.replace(k, v)
        text = non_alpha.sub('-', text).strip('-')

        return text

    # --- simple stat functions
    def _numbers_from(self, data):
        numbers = [e for e in data if type(e) in [float, int]]
        if len(numbers) != len(data):
            logging.warning("Non-numeric data found during processing")

        return numbers

    def _stat(self, column, fn):
        if column:
          data = self.column(column)
          return fn(self.column(column))
        else:
          numeric_cols = [col for col in self.header if col['type'] is float]
          return [fn(self.column(col['index'])) for col in numeric_cols]

    def avarage(self, column=None):
        def _avarage(data): 
          data = self._numbers_from(data)
          return sum(data) / float(len(data))

        return self._stat(column, _avarage)

    def median(self, column=None):
        def _median(data):
          data = self._numbers_from(data)
          if len(data) % 2 == 0:
            hi_mid = data[len(data)/2]
            lo_mid = data[len(data)/2-1]
            return (lo_mid + hi_mid) / 2.0
          else:
            return data[len(data)/2]

        return self._stat(column, _median)

    def summary(self, column=None):
        if column:
          sumstr = u'''
            --------------------
            name: {0}
            max: {1}
            min: {2}
            med: {3:.2f} ({4:.2f}% of ava)
            ava: {5:.2f}
            --------------------
          '''.format(self.header[column]['name'],
                     self.max_value(column),
                     self.min_value(column),
                     self.median(column),
                     (self.median(column)/self.avarage(column)) * 100,
                     self.avarage(column)).rstrip()
          print sumstr
        else:
          for column in [c for c in self.header if c['type'] in [int, float]]:
            self.summary(column['index'])


    def max_value(self, column=None, as_dict=False):
        return self._dispatch_min_max(column, as_dict, lambda a,b: a > b)

    def min_value(self, column=None, as_dict=False):
        return self._dispatch_min_max(column, as_dict, lambda a,b: a < b)

    def _dispatch_min_max(self, column, as_dict, comp):
        # single column
        if column:
          return self._min_max(column, as_dict, comp)
        # all numeric columns
        else:
          numeric_cols = [col for col in self.header if col['type'] is float]
          return [self._min_max(col['index'], as_dict, comp) for col in numeric_cols]

    def _min_max(self, column, as_dict, comp):
        if type(column) in [int, float]:
          col = self.header[column]
        else:
          col = [e for e in self.header if e['slug'] == column].pop()

        max_val = {
          'value'    : self.value(0, col['index']),
          'col_index': col['index'],
          'col_slug': col['slug'],
          'row_index': 0
        }

        for i,v in enumerate(self.column(col['index'])):
          if comp(v, max_val['value']):
            max_val['value']     = v
            max_val['row_index'] = i

        return max_val if as_dict else max_val['value']


# these classes come from Python 2.7 csv documentation
class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def next(self):
        line = self.reader.next().encode("utf-8").strip()
        while line.startswith('#') or not line:
            line = self.reader.next().encode("utf-8").strip()

        return line

    def __iter__(self):
        return self


class UnicodeReader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") if type(s) is str else s for s in row]

    def __iter__(self):
        return self


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
