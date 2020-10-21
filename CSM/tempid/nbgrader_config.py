c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.Exchange.course_id = "tempid"

# Update this list with other assignments you want
c.CourseDirectory.db_assignments = [dict(name="ps1")]

# Change the students in this list with that actual students in
# your course
c.CourseDirectory.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]

c.IncludeHeaderFooter.header = "source/header.ipynb"

###############################################################################
# End additions by nbgrader quickstart
###############################################################################

# Configuration file for nbgrader.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------

## This is an application.

## The date format used by logging formatters for %(asctime)s
#c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#c.Application.log_level = 30

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------

## Base class for Jupyter applications

## Answer yes to any prompts.
#c.JupyterApp.answer_yes = False

## Full path of a config file.
#c.JupyterApp.config_file = ''

## Specify a config file to load.
#c.JupyterApp.config_file_name = ''

## Generate default config file.
#c.JupyterApp.generate_config = False

#------------------------------------------------------------------------------
# NbGrader(JupyterApp) configuration
#------------------------------------------------------------------------------

## A base class for all the nbgrader apps.

## Name of the logfile to log to.
#c.NbGrader.logfile = '.nbgrader.log'

#------------------------------------------------------------------------------
# NbGraderApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# CourseDirectory(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## The assignment name. This MUST be specified, either by setting the config
#  option, passing an argument on the command line, or using the --assignment
#  option on the command line.
#c.CourseDirectory.assignment_id = ''

## The name of the directory that contains assignment submissions after they have
#  been autograded. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.autograded_directory = 'autograded'

## A list of assignments that will be created in the database. Each item in the
#  list should be a dictionary with the following keys:
#  
#      - name
#      - duedate (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Assignment` database model for details on these fields.
#c.CourseDirectory.db_assignments = []

## A list of student that will be created in the database. Each item in the list
#  should be a dictionary with the following keys:
#  
#      - id
#      - first_name (optional)
#      - last_name (optional)
#      - email (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Student` database model for details on these fields.
#c.CourseDirectory.db_students = []

## URL to the database. Defaults to sqlite:///<root>/gradebook.db, where <root>
#  is another configurable variable.
#c.CourseDirectory.db_url = ''

## Format string for the directory structure that nbgrader works over during the
#  grading process. This MUST contain named keys for 'nbgrader_step',
#  'student_id', and 'assignment_id'. It SHOULD NOT contain a key for
#  'notebook_id', as this will be automatically joined with the rest of the path.
#c.CourseDirectory.directory_structure = '{nbgrader_step}/{student_id}/{assignment_id}'

## The name of the directory that contains assignment feedback after grading has
#  been completed. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.feedback_directory = 'feedback'

## List of file names or file globs to be ignored when copying directories.
#c.CourseDirectory.ignore = ['.ipynb_checkpoints', '*.pyc', '__pycache__']

## File glob to match notebook names, excluding the '.ipynb' extension. This can
#  be changed to filter by notebook.
#c.CourseDirectory.notebook_id = '*'

## The name of the directory that contains the version of the assignment that
#  will be released to students. This corresponds to the `nbgrader_step` variable
#  in the `directory_structure` config option.
#c.CourseDirectory.release_directory = 'release'

## The root directory for the course files (that includes the `source`,
#  `release`, `submitted`, `autograded`, etc. directories). Defaults to the
#  current working directory.
#c.CourseDirectory.root = ''

## The name of the directory that contains the master/instructor version of
#  assignments. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#c.CourseDirectory.source_directory = 'source'

## File glob to match student IDs. This can be changed to filter by student.
#  Note: this is always changed to '.' when running `nbgrader assign`, as the
#  assign step doesn't have any student ID associated with it.
#  
#  If the ID is purely numeric and you are passing it as a flag on the command
#  line, you will need to escape the quotes in order to have it detected as a
#  string, for example `--student=""12345""`. See:
#  
#      https://github.com/jupyter/nbgrader/issues/743
#  
#  for more details.
#c.CourseDirectory.student_id = '*'

## The name of the directory that contains assignments that have been submitted
#  by students for grading. This corresponds to the `nbgrader_step` variable in
#  the `directory_structure` config option.
#c.CourseDirectory.submitted_directory = 'submitted'

#------------------------------------------------------------------------------
# FetchApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# QuickStartApp(NbGrader) configuration
#------------------------------------------------------------------------------

## Whether to overwrite existing files
#c.QuickStartApp.force = False

#------------------------------------------------------------------------------
# ValidateApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# ListApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# ReleaseApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# ExtensionApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# AssignApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# SubmitApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FormgradeApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# CollectApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# DbApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# FeedbackApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# ExportApp(NbGrader) configuration
#------------------------------------------------------------------------------

## The plugin class for exporting the grades.
#c.ExportApp.plugin_class = 'nbgrader.plugins.export.CsvExportPlugin'

#------------------------------------------------------------------------------
# ZipCollectApp(NbGrader) configuration
#------------------------------------------------------------------------------

## The name of the directory that contains assignment submission files and/or
#  archives (zip) files manually downloaded from a LMS. This corresponds to the
#  `collect_step` variable in the `collect_structure` config option.
#c.ZipCollectApp.archive_directory = 'archive'

## Format string for the directory structure that nbgrader works over during the
#  zip collect process. This MUST contain named keys for 'downloaded',
#  'assignment_id', and 'collect_step'.
#c.ZipCollectApp.collect_directory_structure = '{downloaded}/{assignment_id}/{collect_step}'

## The plugin class for processing the submitted file names after they have been
#  extracted into the `extracted_directory`.
#c.ZipCollectApp.collector_plugin = 'nbgrader.plugins.zipcollect.FileNameCollectorPlugin'

## The main directory that corresponds to the `downloaded` variable in the
#  `collect_structure` config option.
#c.ZipCollectApp.downloaded_directory = 'downloaded'

## The name of the directory that contains assignment submission files extracted
#  or copied from the `archive_directory`. This corresponds to the `collect_step`
#  variable in the `collect_structure` config option.
#c.ZipCollectApp.extracted_directory = 'extracted'

## The plugin class for extracting the archive files in the `archive_directory`.
#c.ZipCollectApp.extractor_plugin = 'nbgrader.plugins.zipcollect.ExtractorPlugin'

## Force overwrite of existing files.
#c.ZipCollectApp.force = False

## Skip submitted notebooks with invalid names.
#c.ZipCollectApp.strict = False

#------------------------------------------------------------------------------
# AutogradeApp(NbGrader) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# UpdateApp(NbGrader) configuration
#------------------------------------------------------------------------------

## whether to validate metadata after updating it
#c.UpdateApp.validate = True

#------------------------------------------------------------------------------
# ExportPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Base class for export plugins.

## destination to export to
#c.ExportPlugin.to = ''

#------------------------------------------------------------------------------
# CsvExportPlugin(ExportPlugin) configuration
#------------------------------------------------------------------------------

## CSV exporter plugin.

#------------------------------------------------------------------------------
# ExtractorPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Submission archive files extractor plugin for the
#  :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`. Extractor plugin
#  subclasses MUST inherit from this class.

## Force overwrite of existing files.
#c.ExtractorPlugin.force = False

## List of valid archive (zip) filename extensions to extract. Any archive (zip)
#  files with an extension not in this list are copied to the
#  `extracted_directory`.
#c.ExtractorPlugin.zip_ext = ['.zip', '.gz']

#------------------------------------------------------------------------------
# FileNameCollectorPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Submission filename collector plugin for the
#  :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`. Collect plugin subclasses
#  MUST inherit from this class.

## This regular expression is applied to each submission filename and MUST be
#  supplied by the instructor. This regular expression MUST provide the
#  `(?P<student_id>...)` and `(?P<file_id>...)` named group expressions.
#  Optionally this regular expression can also provide the `(?P<first_name>...)`,
#  `(?P<last_name>...)`, `(?P<email>...)`, and `(?P<timestamp>...)` named group
#  expressions. For example if the filename is:
#  
#      `ps1_bitdiddle_attempt_2016-01-30-15-00-00_problem1.ipynb`
#  
#  then this `named_regexp` could be:
#  
#      ".*_(?P<student_id>\w+)_attempt_(?P<timestamp>[0-9\-]+)_(?P<file_id>\w+)"
#  
#  For named group regular expression examples see
#  https://docs.python.org/howto/regex.html
#c.FileNameCollectorPlugin.named_regexp = ''

## List of valid submission filename extensions to collect. Any submitted file
#  with an extension not in this list is skipped.
#c.FileNameCollectorPlugin.valid_ext = ['.ipynb']

#------------------------------------------------------------------------------
# LateSubmissionPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------

## Predefined methods for assigning penalties for late submission

## The method for assigning late submission penalties:
#      'none': do nothing (no penalty assigned)
#      'zero': assign an overall score of zero (penalty = score)
#c.LateSubmissionPlugin.penalty_method = 'none'

#------------------------------------------------------------------------------
# NbConvertBase(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Global configurable class for shared config
#  
#  Useful for display data priority that might be used by many transformers

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#c.NbConvertBase.default_language = 'ipython'

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#c.NbConvertBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#------------------------------------------------------------------------------
# Preprocessor(NbConvertBase) configuration
#------------------------------------------------------------------------------

## A configurable preprocessor
#  
#  Inherit from this class if you wish to have configurability for your
#  preprocessor.
#  
#  Any configurable traitlets this class exposed will be configurable in profiles
#  using c.SubClassName.attribute = value
#  
#  you can overwrite :meth:`preprocess_cell` to apply a transformation
#  independently on each cell or :meth:`preprocess` if you prefer your own logic.
#  See corresponding docstring for informations.
#  
#  Disabled by default and can be enabled via the config by
#      'c.YourPreprocessorName.enabled = True'

## 
#c.Preprocessor.enabled = False

#------------------------------------------------------------------------------
# NbGraderPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Whether to use this preprocessor when running nbgrader
#c.NbGraderPreprocessor.enabled = True

#------------------------------------------------------------------------------
# AssignLatePenalties(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for assigning penalties for late submissions to the database

## The plugin class for assigning the late penalty for each notebook.
#c.AssignLatePenalties.plugin_class = 'nbgrader.plugins.latesubmission.LateSubmissionPlugin'

#------------------------------------------------------------------------------
# IncludeHeaderFooter(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for adding header and/or footer cells to a notebook.

## Path to footer notebook, relative to the root of the course directory
#c.IncludeHeaderFooter.footer = ''

## Path to header notebook, relative to the root of the course directory
#c.IncludeHeaderFooter.header = ''

#------------------------------------------------------------------------------
# LockCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for making cells undeletable.

## Whether all assignment cells are locked (non-deletable and non-editable)
#c.LockCells.lock_all_cells = False

## Whether grade cells are locked (non-deletable)
#c.LockCells.lock_grade_cells = True

## Whether readonly cells are locked (non-deletable and non-editable)
#c.LockCells.lock_readonly_cells = True

## Whether solution cells are locked (non-deletable and non-editable)
#c.LockCells.lock_solution_cells = True

#------------------------------------------------------------------------------
# ClearSolutions(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## The delimiter marking the beginning of a solution
#c.ClearSolutions.begin_solution_delimeter = 'BEGIN SOLUTION'

## The code snippet that will replace code solutions
#c.ClearSolutions.code_stub = {'python': '# YOUR CODE HERE\nraise NotImplementedError()'}

## The delimiter marking the end of a solution
#c.ClearSolutions.end_solution_delimeter = 'END SOLUTION'

## Whether or not to complain if cells containing solutions regions are not
#  marked as solution cells. WARNING: this will potentially cause things to break
#  if you are using the full nbgrader pipeline. ONLY disable this option if you
#  are only ever planning to use nbgrader assign.
#c.ClearSolutions.enforce_metadata = True

## The text snippet that will replace written solutions
#c.ClearSolutions.text_stub = 'YOUR ANSWER HERE'

#------------------------------------------------------------------------------
# SaveAutoGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for saving out the autograder grades into a database

#------------------------------------------------------------------------------
# ComputeChecksums(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to compute checksums of grade cells.

#------------------------------------------------------------------------------
# SaveCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to save information about grade and solution cells.

#------------------------------------------------------------------------------
# OverwriteCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to overwrite information about grade and solution cells.

#------------------------------------------------------------------------------
# CheckCellMetadata(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for checking that grade ids are unique.

#------------------------------------------------------------------------------
# ExecutePreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Executes all the cells in a notebook

## If `False` (default), when a cell raises an error the execution is stopped and
#  a `CellExecutionError` is raised. If `True`, execution errors are ignored and
#  the execution is continued until the end of the notebook. Output from
#  exceptions is included in the cell output in both cases.
#c.ExecutePreprocessor.allow_errors = False

## If execution of a cell times out, interrupt the kernel and continue executing
#  other cells rather than throwing an error and stopping.
#c.ExecutePreprocessor.interrupt_on_timeout = False

## The time to wait (in seconds) for IOPub output. This generally doesn't need to
#  be set, but on some slow networks (such as CI systems) the default timeout
#  might not be long enough to get all messages.
#c.ExecutePreprocessor.iopub_timeout = 4

## The kernel manager class to use.
#c.ExecutePreprocessor.kernel_manager_class = 'builtins.object'

## Name of kernel to use to execute the cells. If not set, use the kernel_spec
#  embedded in the notebook.
#c.ExecutePreprocessor.kernel_name = ''

## If `False` (default), then the kernel will continue waiting for iopub messages
#  until it receives a kernel idle message, or until a timeout occurs, at which
#  point the currently executing cell will be skipped. If `True`, then an error
#  will be raised after the first timeout. This option generally does not need to
#  be used, but may be useful in contexts where there is the possibility of
#  executing notebooks with memory-consuming infinite loops.
#c.ExecutePreprocessor.raise_on_iopub_timeout = False

## If `graceful` (default), then the kernel is given time to clean up after
#  executing all cells, e.g., to execute its `atexit` hooks. If `immediate`, then
#  the kernel is signaled to immediately terminate.
#c.ExecutePreprocessor.shutdown_kernel = 'graceful'

## The time to wait (in seconds) for the kernel to start. If kernel startup takes
#  longer, a RuntimeError is raised.
#c.ExecutePreprocessor.startup_timeout = 60

## The time to wait (in seconds) for output from executions. If a cell execution
#  takes longer, an exception (TimeoutError on python 3+, RuntimeError on python
#  2) is raised.
#  
#  `None` or `-1` will disable the timeout. If `timeout_func` is set, it
#  overrides `timeout`.
#c.ExecutePreprocessor.timeout = 30

## A callable which, when given the cell source as input, returns the time to
#  wait (in seconds) for output from cell executions. If a cell execution takes
#  longer, an exception (TimeoutError on python 3+, RuntimeError on python 2) is
#  raised.
#  
#  Returning `None` or `-1` will disable the timeout for the cell. Not setting
#  `timeout_func` will cause the preprocessor to default to using the `timeout`
#  trait for all cells. The `timeout_func` trait overrides `timeout` if it is not
#  `None`.
#c.ExecutePreprocessor.timeout_func = None

#------------------------------------------------------------------------------
# Execute(NbGraderPreprocessor,ExecutePreprocessor) configuration
#------------------------------------------------------------------------------

## The number of times to try re-executing the notebook before throwing an error.
#  Generally, this shouldn't need to be set, but might be useful for CI
#  environments when tests are flaky.
#c.Execute.execute_retries = 0

## A list of extra arguments to pass to the kernel. For python kernels, this
#  defaults to ``--HistoryManager.hist_file=:memory:``. For other kernels this is
#  just an empty list.
#c.Execute.extra_arguments = []

#------------------------------------------------------------------------------
# GetGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for saving grades from the database to the notebook

## 
#c.GetGrades.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

#------------------------------------------------------------------------------
# ClearOutputPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------

## Removes the output from all code cells in a notebook.

## 
#c.ClearOutputPreprocessor.remove_metadata_fields = {'scrolled', 'collapsed'}

#------------------------------------------------------------------------------
# ClearOutput(NbGraderPreprocessor,ClearOutputPreprocessor) configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# LimitOutput(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## Preprocessor for limiting cell output

## maximum number of lines of output (-1 means no limit)
#c.LimitOutput.max_lines = 1000

## maximum number of traceback lines (-1 means no limit)
#c.LimitOutput.max_traceback = 100

#------------------------------------------------------------------------------
# DeduplicateIds(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor to overwrite information about grade and solution cells.

#------------------------------------------------------------------------------
# ClearHiddenTests(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## The delimiter marking the beginning of hidden tests cases
#c.ClearHiddenTests.begin_test_delimeter = 'BEGIN HIDDEN TESTS'

## The delimiter marking the end of hidden tests cases
#c.ClearHiddenTests.end_test_delimeter = 'END HIDDEN TESTS'

## Whether or not to complain if cells containing hidden test regions are not
#  marked as grade cells. WARNING: this will potentially cause things to break if
#  you are using the full nbgrader pipeline. ONLY disable this option if you are
#  only ever planning to use nbgrader assign.
#c.ClearHiddenTests.enforce_metadata = True

#------------------------------------------------------------------------------
# OverwriteKernelspec(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------

## A preprocessor for checking the notebook kernelspec metadata.

#------------------------------------------------------------------------------
# Exchange(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#c.Exchange.cache = ''

## A key that is unique per instructor and course. This MUST be specified, either
#  by setting the config option, or using the --course option on the command
#  line.
#c.Exchange.course_id = ''

## Whether the path for fetching/submitting  assignments should be prefixed with
#  the course name. If this is `False`, then the path will be something like
#  `./ps1`. If this is `True`, then the path will be something like
#  `./course123/ps1`.
#c.Exchange.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#c.Exchange.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#c.Exchange.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#c.Exchange.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeCollect(Exchange) configuration
#------------------------------------------------------------------------------

## Update existing submissions with ones that have newer timestamps.
#c.ExchangeCollect.update = False

#------------------------------------------------------------------------------
# ExchangeFetch(Exchange) configuration
#------------------------------------------------------------------------------

## Whether to replace missing files on fetch
#c.ExchangeFetch.replace_missing_files = False

#------------------------------------------------------------------------------
# ExchangeList(Exchange) configuration
#------------------------------------------------------------------------------

## List assignments in submission cache.
#c.ExchangeList.cached = False

## List inbound files rather than outbound.
#c.ExchangeList.inbound = False

## Remove, rather than list files.
#c.ExchangeList.remove = False

#------------------------------------------------------------------------------
# ExchangeRelease(Exchange) configuration
#------------------------------------------------------------------------------

## Force overwrite existing files in the exchange.
#c.ExchangeRelease.force = False

#------------------------------------------------------------------------------
# ExchangeSubmit(Exchange) configuration
#------------------------------------------------------------------------------

## Whether or not to submit the assignment if there are missing notebooks from
#  the released assignment notebooks.
#c.ExchangeSubmit.strict = False

#------------------------------------------------------------------------------
# BaseConverter(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## Whether to overwrite existing assignments/submissions
#c.BaseConverter.force = False

## Permissions to set on files output by nbgrader. The default is generally read-
#  only (444), with the exception of nbgrader assign and nbgrader feedback, in
#  which case the user also has write permission.
#c.BaseConverter.permissions = 0

#------------------------------------------------------------------------------
# Assign(BaseConverter) configuration
#------------------------------------------------------------------------------

## Whether to create the assignment at runtime if it does not already exist.
#c.Assign.create_assignment = False

## Do not save information about the assignment into the database.
#c.Assign.no_database = False

#------------------------------------------------------------------------------
# Autograde(BaseConverter) configuration
#------------------------------------------------------------------------------

## Whether to create the student at runtime if it does not already exist.
#c.Autograde.create_student = False

#------------------------------------------------------------------------------
# Feedback(BaseConverter) configuration
#------------------------------------------------------------------------------
