<h1 align=center>
	Mob Farm Autoclicker
</h1>

<p align=center>
	A simple python autoclicker built with the mouse library for Minecraft mob farming.
</p>

<div align="center">
	<img src="./img/run-demo.gif">
</div>

### Setup

There is one python package required for this script to work:

- mouse

To set up the environment, install the package according to `requirements.txt`:

```
$ pip3 install -r requirements.txt
```

### Usage

#### Run

Just run `main.py` and that's it.

Since the script makes use of the `_os_mouse` module, it does not matter what value your "Raw Input" Minecraft setting is set to. The mouse will do its thing anyway.

#### Settings

The default settings were calibrated to perform in the "Hard" Minecraft difficulty mode. If needed, change them to suit your game:

- `ACTION_DELAY_SEC` = delay between each attack action (default 45);
- `ATTACK_DELAY_SEC` = delay between each individual attack (min 0.625 -> the sword attack cooldown duration; default 0.625 + 0.125);
- `ATTACKS_PER_TRY` = how many times to perform an attack sequence during an attack action (default 3);
- `X_OFFSET` = mouse offset amount in px (default 75).
