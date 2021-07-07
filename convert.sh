#!/bin/bash
cat papers.bib | bibtex2html -nolinks -noabstract | tail -n +2 > papers.html

