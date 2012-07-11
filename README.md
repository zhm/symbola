# Symbola - an icon font for maps

This is a font made from public domain SVG's. The designers deserve all of the credit,
I'm just packaging them into fonts.

- [Maki](https://github.com/mapbox/maki/)
- [AIGA](http://thenounproject.com/collections/aiga/)
- [National Park Service](http://thenounproject.com/collections/national-park-service/)

This font allows you to manage symbology in the datasource and helps reduce duplication
in your carto stylesheet. Using a font for the icons also lets you easily change the colors
of the symbols on your map using the standard `text-fill` attribute in TileMill. In fact
all of the Mapnik text effects will work on the icons.

# Usage
Doing symbols with fonts like this isn't perfect and does require you to have specific unicode
attributes in your data. So it doesn't get rid of the problem of mapping data to symbols,
but it does let you manage it in the database so you can update symbology using SQL instead of
having a lot of duplication in your carto stylesheet. It's likely that future versions of carto and
Mapnik will improve this.

It's possible to use this technique with any datasource as long as you can store unicode characters
in the data.

## PostGIS
First, you will need to add a column to your table to hold the character for the icon for
each row. Here I have a table named `atons_geo` with some navigation aids in it.

    ALTER TABLE atons_geo ADD icon text;

Now that you have a column to hold the icon attribute, you can put some data into it. You can lookup
the hex codes for each icon on the [web site](http://zhm.github.com/symbola/) by hovering on the icon.
How you want to do your symbology is entirely up to you. My table actually had a column named `symbol`, so
that seems like a good fit:

    UPDATE atons_geo SET icon=chr(x'2100'::int) WHERE symbol='RRL-O';
    UPDATE atons_geo SET icon=chr(x'2101'::int) WHERE symbol='LT-E';
    UPDATE atons_geo SET icon=chr(x'2102'::int) WHERE symbol='LT';
    UPDATE atons_geo SET icon=chr(x'2103'::int) WHERE symbol='LBB-O';
    UPDATE atons_geo SET icon=chr(x'2104'::int) WHERE symbol='LWB-O';
    UPDATE atons_geo SET icon=chr(x'2105'::int) WHERE symbol='N-E';

Now that the data is in the database, add it as a layer to your TileMill project. I added one
called `atons`. Here is my stylesheet that makes use of the icons:

    #atons {
      marker-width: 0;
      marker-allow-overlap: true;
      text-allow-overlap: true;
      text-face-name: "Symbola Medium";
      text-name: "[icon]";
      text-size: 24;
      text-placement: point;
      text-fill: #111111;
      text-halo-radius: 0.5;
      text-halo-fill: #333333;
    }


# Adding New Icons
First, you will need to install fontforge. On a Mac, that's easy:

    brew update && brew install fontforge

This will give you a `fontforge` command that's required for building the font files.

To build the font files, simply run:

    make

To delete the fonts:

    make clean

To add new icons, just add more svg files to the `svg` directory. Right now the `generate.py` script is fairly
brittle, so the file names must be sequential. The font glyphs start at 0x2100 (8448 decimal). So take the svg
number and add 8448 to it to get the unicode character required for your icon. Don't forget to convert that number
back to hex if you use the PostgreSQL syntax above.
