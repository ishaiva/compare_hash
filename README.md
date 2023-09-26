# Hash Comparison Tool

The Hash Comparison Tool is a command-line utility that allows you to compare hash values of strings or files. Hash values are unique representations of data, generated using hash algorithms. This tool can be used to verify data integrity and authenticity by comparing hash values.

## Features

- Compare two hash values.
- Compare a file's content with a hash value.
- Compare contents of two files.
- Supports various hash algorithms (MD5, SHA-1, SHA-256, etc.).

## Usage

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the tool's script.
4. Run the script using the following command:

   ```bash
   python hash_comparison.py

Options

   Match two hash values: Manually input two hash values and compare them.
   Match a file's content with a hash value: Compare a file's content hash with a provided hash value. Choose a hash algorithm from the list.
   Match a file's content with another file's content: Compare the content hashes of two files.
   Exit: Quit the program.


Dependencies

   Python 3.x
   hashlib library (comes with Python)

Color Codes

The tool uses color codes for clearer visual feedback:

   Green: Hashes or contents match.
    Red: Hashes or contents do not match.

Contribution

Feel free to contribute to this project by adding new features, improving documentation, or fixing issues. Create a pull request with your changes.
License

This tool is open-source and distributed under the MIT License.

MIT License

Copyright (c) [2023] [ishaiva]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
