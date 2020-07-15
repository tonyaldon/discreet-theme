# About

`discreet-theme` is a dark theme for [Highlight.js](http://highlightjs.org).

This theme is close to the theme a I'm using within emacs. See my
[emacs config](https://github.com/tonyaldon/emacs.d).

# Motivation

There already exists cool dark themes out there for highlightjs (see
[highlightjs demo](https://highlightjs.org/static/demo/)), but for
concistency I wanted the one I use everyday within emacs.

# Install

1. Copy `discreet-theme.css` to your desired directory.

2. Include the theme in your html and turn on highlightjs.

		<link rel="stylesheet" href="discreet-theme.css">
		<script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/10.1.1/highlight.min.js"></script>
		<script>hljs.initHighlightingOnLoad();</script>

# Dev

The `dev/public/index.html` contains some chunks of code (`bash`,
`html`, `css`, `javascript`, `python`) and can be serve as static
files with `express`. To do so, follow the 3 steps below.

1. Install dev depencies by running the command:

		npm install

2. Serve the app and watch the files by running the command:

		npm run dev

3. Open the `index.html` in your browser at the url `localhost:3000/index.html`.
