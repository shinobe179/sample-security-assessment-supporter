## AI Security Assessment Supporter

Once you submit an website URL of SaaS, AI supporter will research and response what security standards it have.

# How to run

prerequirement: [uv](https://github.com/astral-sh/uv) is already installed.

```
$ uv sync
$ uv .venv/bin/activate
$ playwright install # only at once
$ export OPENAI_API_KEY=foobar # use your API key
$ streamlit run app.py
```

Then the web page will be launched.
