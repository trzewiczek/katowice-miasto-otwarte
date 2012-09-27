import csv, codecs, cStringIO

class Table:
  '''
  Table class provides a simple abstraction over a csv files with
  easy access to rows, columns and single cells as values or dicts.
  Along with that Table class provides a basic statistics (min/max,
  median, avarage) over table columns as well as cool summary report.
  '''
  def __init__(self, path, **kwargs):
    '''
    Table constructor reads data from csv file specified in the path
    parameter. The file has to be utf-8 encoded. All cells that are
    not enclosed in <quotechar> will be automaticaly converted into 
    numeric (float) values. 
    The default parameters are:
      - delimiter (';' by default)
      - quotechar ('"' by default)
      - quoting   (NON_NUMERIC by default)
      - header    (False by default)
    If the header is True, the first row in the file will be used
    as labels of columns and keys in as_dict representaion of data.
    '''
    # override the default options
    csv_opts, oth_opts = self._get_opts(kwargs)

    # read the csv file and clean the data
    reader = UnicodeReader(open(path), **csv_opts)
    rows   = self._clean_data(reader)

    # initialize the table
    if oth_opts['header']:
      self.data   = rows[1:]
      self.header = []
      for i,(h,v) in enumerate(zip(rows[0], rows[1])):
        column = {
          'index': i,
          'label': h,
          'type' : type(v)
        }
        self.header.append(column)
    else:
      self.data   = rows
      self.header = None

    # cast to proper datatypes
    self.rows_count = len(self.data)
    self.cols_count = len(self.data[0])


  def value(self, row, column):
    '''
    Returns a value of a specified cell in the table. The column
    parameter can be either number (index) or string/unicode (label)
    '''
    as_dict = type(column) in [str, unicode]

    return self.row(row, as_dict=as_dict)[column]

  def _stat(self, column, fn):
    if column:
      data = self.column(column)
      return fn(self.column(column))
    else:
      numeric_cols = [col for col in self.header if col['type'] is float]
      return [fn(self.column(col['index'])) for col in numeric_cols]

  def avarage(self, column=None):
    '''
    Returns an avarage of the single column (if provided) or
    for all columns in the table (as a list of medians)
    '''
    def _avarage(data): 
      return sum(data) / float(len(data))

    return self._stat(column, _avarage)

  def median(self, column=None):
    '''
    Returns a median of the single column (if provided) or
    for all columns in the table (as a list of medians)
    '''
    def _median(data):
      if len(data) % 2 == 0:
        hi_mid = data[len(data)/2]
        lo_mid = data[len(data)/2-1]
        return (lo_mid + hi_mid) / 2.0
      else:
        return data[len(data)/2]

    return self._stat(column, _median)

  def summary(self, column=None):
    '''
    Prints a nice summary of a single column (if provided) or 
    all the columns in the table (if a column index not provided)
    '''
    if column:
      sumstr = '''
        --------------------
        label: {0}
        max: {1}
        min: {2}
        med: {3} ({4:.2f}% of ava)
        ava: {5}
        --------------------
      '''.format(self.header[column]['label'],
                 self.max_value(column),
                 self.min_value(column),
                 self.median(column),
                 (self.median(column)/self.avarage(column)) * 100,
                 self.avarage(column)).rstrip()
      print sumstr
    else:
      for column in [c for c in self.header if c['type'] is float]:
        self.summary(column['index'])

  def row(self, index, as_dict=False):
    '''
    Returns a single row as a list of values or a dict with columns
    labels as keys.
    '''

    row = self.data[index]
    return self._make_dict(row) if as_dict else row

  def rows(self, as_dict=False):
    '''
    Returns a list of all rows. Each row can be serialized as a list 
    of values or a dict with columns labels as keys.
    '''
    return [self._make_dict(row) for row in self.data] if as_dict else self.data

  def column(self, column, as_dict=False):
    '''
    Returns a single column as a list of values or a dict (if as_dict=True):
      
      {
        'label': 'some_label',
        'index': 3,
        'type' : float,
        'values': [ 1, 2, 3, 4, 5 ]
      }

    The column can be specified as a numeric index or string/unicode label.
    '''
    if type(column) in [str, unicode]:
      col = dict([e for e in self.header if e['label'] == column].pop())
    else:
      col = self.header[column]
    data = [row[col['index']] for row in self.data]

    if as_dict:
      col['values'] = data
      return col
    else:
      return data

  def columns(self, as_dict=False):
    '''
    Returns a list of columns. It can be serialized as a list
    of lists or as a list of dicts if as_dict=True.
    '''

    return [self.column(c['label'] if as_dict else c['index']) for c in self.header]

  
  def _make_dict(self, row):
    if self.header:
      return {k['label']: v for k,v in zip(self.header, row)}
    else:
      return {'col'+str(i): v for i,v in enumerate(row)}

  def max_value(self, column=None, as_dict=False):
    '''
    Finds the maximum value among the numeric columns. If a specific
    column is provided, it returns only max value in this column. 
    The column can be specified by the index or label. 
       
       my_table.max_value()         -->  list of max values
       my_table.max_value(3)        -->  max value in col 3
       my_table.max_value('price')  -->  max value in col 'price'

    Adding a as_dict=True to any of these calls returns the same
    results, but serialized as dicts.
    '''
    return self._dispatch_min_max(column, as_dict, lambda a,b: a > b)

  def min_value(self, column=None, as_dict=False):
    '''
    Finds the minimum value among the numeric columns. If a specific
    column is provided, it returns only min value in this column. 
    The column can be specified by the index or label. 
       
       my_table.min_value()         -->  list of min values
       my_table.min_value(3)        -->  min value in col 3
       my_table.min_value('price')  -->  min value in col 'price'

    Adding a as_dict=True to any of these calls returns the same
    results, but serialized as dicts.
    '''
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
      col = [e for e in self.header if e['label'] == column].pop()

    max_val = {
      'value'    : self.value(0, col['index']),
      'col_index': col['index'],
      'col_label': col['label'],
      'row_index': 0
    }

    for i,v in enumerate(self.column(col['index'])):
      if comp(v, max_val['value']):
        max_val['value']     = v
        max_val['row_index'] = i

    return max_val if as_dict else max_val['value']

  def _get_opts(self, opts):
    csv_opts = {
      'delimiter': opts.get('delimiter', ';'),
      'quotechar': opts.get('quotechar', '"'),
      'quoting'  : opts.get('quoting', csv.QUOTE_NONNUMERIC)
    }
    oth_opts = {
      'header': opts.get('header', False),
    }
    
    return (csv_opts, oth_opts)

  def _clean_data(self, data):
    clean_data = []

    for row in data:
      # ommit blank lines and comments
      if len(row) == 0 or (type(row) is str and row[0].startswith('#')):
        continue

      # strip and remove internal new lines from string cells
      clean_row = []
      for cell in row:
        if type(cell) is str:
          cell = cell.strip().replace('\n',' ')

        clean_row.append(cell)

      clean_data.append(clean_row)

    return clean_data


class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

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

