The algorithm works by adding a parity bit to each position of 2<sup>N</sup>, where N is starting from zero, SO:

- 2<sup>0</sup> = 1
- 2<sup>1</sup> = 2
- 2<sup>2</sup> = 4
- and so on ...

databits are then arranged accordingly to the 'open' positions:
| Bit position| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|-----|-----|-----|-----|-----|------|------|
| Encoded Data Bits| P<sub>1</sub> | P<sub>2</sub> | D<sub>1</sub> | P<sub>4</sub> | D<sub>2</sub> | D<sub>3</sub> | D<sub>4</sub> |
| e.g. input **1011**| 0 | 1 | 1 | 0 | 0 | 1 | 1 |
| e.g. input **1000**| 1 | 1 | 1 | 0 | 0 | 0 | 0 |

The parities numbers are not a coincidence, they represent which data bits that they 'cover':

- P<sub>1</sub>: Starts at it's bit position and checks it, skips one and checks the next, and so on _(bit position: 1, 3, 5, 7, ...)_
- P<sub>2</sub>: Starts at it's bit position and checks two, skips two and so on _(bit position: 2-3, 6-7, 10-11, 14-15, ...)_
- P<sub>4</sub>: Starts at it's bit position and checks four, skips four and so on _(bit position: 4-7, 12-15, 20-23, ... )_

The parity bits are then determined based on these databits that they are 'covering', so e.g.:

- P<sub>1</sub> covers D<sub>1</sub>, D<sub>2</sub>, D<sub>4</sub>: If ones in these databits are odd, the parity will be **1**, if they are even, it will be **0**
  - P<sub>1</sub> = 1 if databits are [1 | 1 | 1] (their are an odd number of ones)
