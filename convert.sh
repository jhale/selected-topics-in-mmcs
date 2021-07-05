#!/bin/bash
cat papers.bib | bibtex2html | tail -n +2 > papers.html

