#!/bin/bash
cat papers.bib | bibtex2html -a -nolinks -noabstract | tail -n +2 > papers.html

