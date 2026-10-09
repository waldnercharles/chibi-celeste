import sys
rows = [r for r in open(sys.argv[1]).read().split('\n') if r]
w = len(rows[0])
sx = sy = 0
lines = []
for y, r in enumerate(rows):
    if 'S' in r:
        sx, sy = r.index('S'), y
    lines.append('            ' + ', '.join('1' if c == '#' else '0' for c in r) + ',')
lines[-1] = lines[-1].rstrip(',')
print('library Room {')
print('    // Tile rows, 1 = solid. Generated from room.txt; S marks the spawn tile.')
print('    function Tiles() -> (tiles: int[]) {')
print('        return [')
print('\n'.join(lines))
print('        ]')
print('    }')
print('')
print('    function Columns() -> (columns: int) {')
print(f'        return {w}')
print('    }')
print('')
print('    function Rows() -> (rows: int) {')
print(f'        return {len(rows)}')
print('    }')
print('')
print('    function Start() -> (feet: CF_V2) {')
print(f'        return vec2({sx * 8 + 4}, {sy * 8 + 8})')
print('    }')
print('}')
