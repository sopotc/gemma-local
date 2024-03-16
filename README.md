#### Pre-reqs

There are a couple of places to register because Google wants to track who gets access to it, mainly for you to sign some EULA before using.

1. Register at Kaggle. Just log in through your Google account and it's nice and easy. Stay logged in.

2. Register and log in at HuggingFace. Should be easy enough. Log in and stay logged in.
    * Go to URL `https://huggingface.co/google/gemma-2b`
    * Under 'Model Card' follow instructions to sign some EULA for Gemma. This will need to quickly use your Kaggle logged-in state to work that you did in 1.
    * Once you're done it should say 'Gated model. You have been granted access to this model.

While still in HuggingFace website go to your account (round avatar on top right corner). Click Settings.
* On the left pane find and click 'Access Tokens'.
* Click 'New Token'. Give it an arbitrary name, with 'read' permission. Click generate and copy the token.
* You'll need this token in your python code so they can map the token with your account and thus the fact that you have access to the model.
* Paste this token into the piece of code that says 'YOUR_TOKEN_HERE'.

#### One-time setup

Run this on the repo root:
* ```python3 -m venv .venv``` to create venv
* `source .venv/bin/activate` to activate above venv
* `pip install -q -U torch transformers accelerate` to install dependencies. It's important for this to be done after source command, otherwise it messes up root env. It's in quiet mode so you won't see much until it's over. Just wait it out.

#### Run
While on repo root activate the venv with `source .venv/bin/activate`.

Simply run `python run.py`