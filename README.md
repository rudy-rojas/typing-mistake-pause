<pre>
<b>Testing in:</b>
<b>Version:</b> Anki 25.02.4 (a5c33ad0)
Python 3.9.18 Qt 6.6.2 PyQt 6.6.1
</pre>


### Typing Mistake Pause (Anki)

<p><b>Version:</b> 1.1</p>
<p><b>Description:</b> Temporarily pauses answer buttons when you type an incorrect answer, giving you time to reflect on your mistake.</p>

#### Features:

<ul>
    <li><code>1200ms</code> pause when answer is incorrect</li>
    <li>Keyboard shortcuts: <code>1</code> (Again), <code>2</code> (Hard), <code>3</code> (Good), <code>4</code> (Easy)</li>
    <li>Buttons are temporarily disabled to prevent rushed responses</li>
</ul>

#### Default Settings:

```python
TIME_PAUSE   = 1200 # miliseconds
AGAIN_OPTION = 1    # Again key
HARD_OPTION  = 2    # Hard key
GOOD_OPTION  = 3    # Good key
EASY_OPTION  = 4    # Easy key
```

## Important:

<p>
<b>Disable</b> (Again, Hard, Good, Easy) in <code>Preferences > Review > Answer keys</code> and <b>restart</b> Anki, otherwise it won't work.
</p>
