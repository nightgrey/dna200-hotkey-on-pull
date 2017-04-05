# dna200-hotkey-on-pull
Reads the serial connection input of a DNA200 device connected via USB. Then triggers the configured keypress as soon as it registers one of two states, namely "pulling" and "not pulling".

This is intended to disable push-to-talk of any voice chat software so I can babble on Discord and comfortably avoid annoying people in the same channel by vaping.

**Credit** goes to [/u/sirus20x6](https://www.reddit.com/user/sirus20x6) who had the idea first and made the [original script](https://www.reddit.com/r/electronic_cigarette/comments/4pw6kq/python_script_to_mute_your_skype_mice_when_you/)!

## Usage
Open [the script](/dna200-hotkey-on-pull.py) and set the [`portName`](/dna200-hotkey-on-pull.py#L27) variable. You can get the name from the Windows *device manager*. Everything else is optional, but you might want to customize the [`hotkey`](/dna200-hotkey-on-pull.py#L33). Keep in mind this is a basic script, but it gets the job done.

**Requirements**
  * Windows (works on Windows 10, 64-bit)
  * Python 2.7 (https://www.python.org/downloads/)
  * Python for Windows Extensions (https://sourceforge.net/projects/pywin32)
  * Pip (https://pip.pypa.io/en/stable/installing/)
  * pyserial (https://github.com/pyserial/pyserial)

## Notes and known problems
  * It can't natively mute your microphone and it can't register different hotkeys for enabling and disabling. It also assumes you are not muted when you start it.
  
## Ideas and improvements
Don't hesitate to make an issue or pull requests if you have any ideas and/or improvements. I'm a newbie when it comes to Python and I'm sure there's a lot that could be done better.

Ideas I've had:
    * Port script to node.js, then create a small electron app bundled with
    everything. THAT WOULD BE SO NOICE - and fun.
    * Cross-compatibility
    * Different actions
    * Native microphone mute (tried it, didn't get it to work)
    * Print connected serial ports
    * Interactive script => configuration via console window
    
## License

Do what you want with it. Na, really. [Go nuts](/LICENSE).
