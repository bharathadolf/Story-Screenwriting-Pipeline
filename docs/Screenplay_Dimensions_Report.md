# 📐 Standard Layout Summary Table

These are the exact dimensions implemented in the generated HTML files, designed around an 8.5" x 11" US Letter page.

| Element           | Left (from edge) | Right (from edge) | CSS Setting                                   |
| :---------------- | :--------------- | :---------------- | :-------------------------------------------- |
| **Page Margin**   | 1.5"             | 1"                | `padding-left: 1.5in; padding-right: 1.0in;`  |
| **Page Numbers**  | (Right aligned)  | 1.0"              | `right: 1.0in; top: 0.5in;`                   |
| **Slugline**      | 1.5"             | 7.5"              | `margin-left: 0in;` (relative to 1.5" margin) |
| **Action**        | 1.5"             | 7.5"              | `margin-left: 0in;` (relative to 1.5" margin) |
| **Character**     | 3.7"             | 5.5"              | `margin-left: 2.2in; width: 1.8in;`           |
| **Dialogue**      | 2.5"             | 6.0"              | `margin-left: 1.0in; width: 3.5in;`           |
| **Parenthetical** | 3.1"             | 5.6"              | `margin-left: 1.6in; width: 2.5in;`           |
| **Transition**    | 6.0"             | 7.5"              | `margin-left: 4.5in; width: 1.5in;`           |

_Note: The generated HTML script utilizes `margin-left` and fixed `width` properties based on the inner padding of the 8.5" page to guarantee block structure and timing accuracy for Courier font._
