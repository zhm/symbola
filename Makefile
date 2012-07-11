all:
	fontforge -script generate.py

clean:
	rm fonts/*

.PHONY: all clean
