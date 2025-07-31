import html
import json
from typing import TYPE_CHECKING, Any, Union

from aqt import gui_hooks, mw
from aqt.reviewer import Reviewer, ReviewerBottomBar
from aqt.qt import QAction
from aqt.utils import showInfo

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
    # typeCorrect = html.unescape(mw.reviewer.typeCorrect.lower())
    typeCorrect = html.unescape(mw.reviewer.typeCorrect)
    # typedAnswer = html.unescape(mw.reviewer.typedAnswer.lower())
    typedAnswer = html.unescape(mw.reviewer.typedAnswer)
    # typeCorrectUnescape = html.unescape(mw.reviewer.typedAnswer)
    typeCorrectUnescape = mw.reviewer.typedAnswer
    # if typedAnswer == typeCorrect and typedAnswer != "":
    if typedAnswer == typeCorrect:
        mw.reviewer.web.eval("document.addEventListener('keydown', keydownHandler);")
        mw.reviewer.web.eval(f'setEscapeTypeCorrect({json.dumps(typeCorrectUnescape)});') # uncomment: import json
        # mw.reviewer.web.eval(f'setEscapeTypeCorrect("{typeCorrect}");')
    elif typeCorrect.lower() != typedAnswer.lower():
        mw.reviewer.bottom.web.eval("disableTempPanel();")
        mw.reviewer.web.eval("disableTempKeydownHandler();")
    else:
        mw.reviewer.web.eval("document.addEventListener('keydown', keydownHandler);")
        # mw.reviewer.web.eval(f'setEscapeTypeCorrect({json.dumps(typeCorrectUnescape)});')

# Older Anki versions
# def init_addon(card) -> None:
#     typeCorrect = html.unescape(mw.reviewer.typeCorrect.lower())
#     typedAnswer = html.unescape(mw.reviewer.typedAnswer.lower())
#     if typedAnswer != typeCorrect:
#         mw.reviewer.bottom.web.eval("disableTempPanel();") 
#         mw.reviewer.web.eval("disableTempKeydownHandler();")
#     else:
#         mw.reviewer.web.eval("document.addEventListener('keydown', keydownHandler);")



def show_plugin_about():
    """Shows information about the plugin"""
    info_text = """
    <h3>Typing Mistake Pause</h3>
    <p><b>Version:</b> 1.0</p>
    <p><b>Description:</b> Temporarily pauses answer buttons when you type an incorrect answer, giving you time to reflect on your mistake.</p>
    
    <h4>Features:</h4>
    <ul>
        <li>{time_pause}ms pause when answer is incorrect</li>
        <li>Keyboard shortcuts: {again} (Again), {hard} (Hard), {good} (Good), {easy} (Easy)</li>
        <li>Buttons are temporarily disabled to prevent rushed responses</li>
    </ul>
    
    <h4>Current Settings:</h4>
    <ul>
        <li><b>Pause Time:</b> {time_pause} milliseconds</li>
        <li><b>Again Key:</b> {again}</li>
        <li><b>Hard Key:</b> {hard}</li>
        <li><b>Good Key:</b> {good}</li>
        <li><b>Easy Key:</b> {easy}</li>
    </ul>
    """.format(
        time_pause=TIME_PAUSE,
        again=AGAIN_OPTION,
        hard=HARD_OPTION,
        good=GOOD_OPTION,
        easy=EASY_OPTION
    )
    
    showInfo(info_text, title="Typing Mistake Pause - Information")

def setup_menu():
    """Sets up the plugin menu"""
    if mw is None:
        return
    
    # Create menu action
    action = QAction("Typing Mistake Pause", mw)
    action.triggered.connect(show_plugin_about)
    
    # Add to Tools menu
    mw.form.menuTools.addAction(action)

gui_hooks.webview_will_set_content.append(on_webview_will_set_content)
gui_hooks.reviewer_did_show_answer.append(init_addon)

# Setup menu when Anki is ready
gui_hooks.main_window_did_init.append(setup_menu)