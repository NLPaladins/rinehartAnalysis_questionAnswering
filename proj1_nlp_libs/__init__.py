"""Top-level package."""

from nlp_libs.fancy_logger import ColorizedLogger
from nlp_libs.configuration import Configuration, validate_json_schema
from nlp_libs.books import ProcessedBook, extract_surnames, obtain_aliases_for_book, get_dictionary_of_named_occurrences, create_alias_occurrence_dictionary


__email__ = "jmerlet@vols.utk.edu, kgeorgio.vols.utk.edu, mlane42@vols.utk.edu"
__author__ = "jeanmerlet, drkostas, LaneMatthewJ"
__version__ = "0.1.0"
