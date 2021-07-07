#!/bin/bash
cat papers.bib | bibtex2html -a -nokeywords -nolinks -noabstract | tail -n +2 > papers.html

