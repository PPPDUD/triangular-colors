# triangular-colors
A small Python script to generate colors whose components represent the side lengths of triangles.

`colors.json` is all of these so-called _triangular colors_ in a single file; each entry is an array where the first value is another array representing an RGB value, and the second value is a string, whose value is "a" for an _acute triangle_, "r" for a _Pythagorean right triangle_, or "o" for an _obtuse triangle_.

`pythagorean.json`, `acute.json`, and `obtuse.json` each contain an array with colors representing their respective types of triangles.

For the purposes of this script, an RGB value is a list of three positive integers from 1 to 255, inclusive.
