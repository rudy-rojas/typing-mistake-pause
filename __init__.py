import html
from typing import TYPE_CHECKING, Any, Union

from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer, ReviewerBottomBar

# from aqt.utils import showInfo
if TYPE_CHECKING:
    from aqt.webview import WebContent
    assert mw is not None

from .consts import MODULE_ADDON 
from .settings import TIME_PAUSE, AGAIN_OPTION, HARD_OPTION, GOOD_OPTION, EASY_OPTION


mw.addonManager.setWebExports(__name__, r"web.*")

reviewer_injector = f"""
<script>
  var time_pause = {TIME_PAUSE};
  var again_option ='{AGAIN_OPTION}';
  var hard_option = '{HARD_OPTION}';
  var good_option = '{GOOD_OPTION}';
  var easy_option = '{EASY_OPTION}';
</script>
<script src="/_addons/{MODULE_ADDON}/web/manage-questions.js"></script>
"""

reviewer_bottom_injector = f"""
<script>
  var time_pause = {TIME_PAUSE};
</script>
<script src="/_addons/{MODULE_ADDON}/web/manage-bottom-bar.js"></script>
"""

def on_webview_will_set_content(
    web_content: "WebContent",
    context: Union[ReviewerBottomBar, Reviewer, Any],
    *args,
):
    if isinstance(context, Reviewer):
        web_content.body += reviewer_injector
    elif isinstance(context, ReviewerBottomBar):
        web_content.body += reviewer_bottom_injector
    else:
        return


def init_addon(card) -> None:
    typeCorrect = html.unescape(mw.reviewer.typeCorrect.lower())
    typedAnswer = html.unescape(mw.reviewer.typedAnswer.lower())
    if typedAnswer != typeCorrect:
        mw.reviewer.bottom.web.eval("disableTempPanel();") 
        mw.reviewer.web.eval("disableTempKeydownHandler();")
    else:
        mw.reviewer.web.eval("document.addEventListener('keydown', keydownHandler);")

gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
gui_hooks.reviewer_did_show_answer.append(init_addon)
