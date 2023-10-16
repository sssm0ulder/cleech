import dataclasses
import re
import urllib.parse
from dataclasses import dataclass

TELEGRAM_SIMPLE_PAGE_PATH_URL_PATTERN = re.compile(r'^/?(?P<page_id>[a-zA-Z0-9_]+)/?$')


@dataclass
class TelegramURLValidator:
    url: str
    DOMAINS = ('t.me', 'telegram.me')

    def __post_init__(self):
        try:
            self.parsed_url = urllib.parse.urlparse(self.url)
        except ValueError as e:
            raise e

    def validate(self) -> bool:
        return self._validate_domain()

    def _validate_domain(self) -> bool:
        if self.parsed_url.netloc in self.DOMAINS:
            return True
        return False

    def _is_valid_url(self) -> bool:
        return self._is_open_page_url() or self.is_invite_page_url()

    def _extract_id_from_url(self, key: str, pattern: re.Pattern) -> str:
        index = pattern.groupindex[key]
        return pattern.match(self.parsed_url.path)[index]  # type: ignore

    def get_channel_id(self) -> str:
        if self._is_simple_page_url():
            return self._extract_id_from_url('page_id', TELEGRAM_SIMPLE_PAGE_PATH_URL_PATTERN)

        raise AssertionError('No branch of code')

    def _is_simple_page_url(self) -> bool:
        return self._match_url_path_pattern(TELEGRAM_SIMPLE_PAGE_PATH_URL_PATTERN)

    def _match_url_path_pattern(self, pattern: re.Pattern) -> bool:
        return bool(pattern.match(self.parsed_url.path))
