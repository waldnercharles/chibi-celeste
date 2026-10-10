# Celeste Movement

Madeline's movement from Celeste, ported to Chibi script. Everything game-specific lives in
`content/`: the engine supplies only input, transforms, shapes and sprites.

- `behaviors/Player.chibi` ports the Normal, Climb and Dash states from
  [NoelFB/Celeste `Player.cs`](https://github.com/NoelFB/Celeste/blob/master/Source/Player/Player.cs):
  run, variable jump, coyote time, jump/dash buffering, wall slide, wall jump, climb, climb hop,
  stamina, 8-way dash with freeze frames, super, hyper and wall-bounce jumps, corner correction and
  ducking. It also simulates Madeline's hair (after `PlayerHair`), which turns blue with no dash left.
- `behaviors/CameraFollow.chibi` eases the camera toward the player inside the room bounds.
- `scenes/Level.kdl` contains the 64×23 test room as editable Tile entities.
  Player collision reads these authored tiles when Play starts; moving or removing
  tiles changes the playable level. Collision follows their exact positions.
  `libraries/Room.chibi` supplies the room bounds.

## Controls

| Action | Keyboard | Gamepad |
|---|---|---|
| Move | WASD | Left stick |
| Jump | Space or C | A |
| Dash | X or K | X |
| Grab | Z or L | Right shoulder |

`content/input.kdl` binds Jump, Dash and Grab, and `Player.chibi` reads them as `input.Jump.held`.
Arrow keys are not movement sources in the engine yet.

## Play and edit in the browser

[Play Celeste](https://waldnercharles.github.io/chibi-celeste/) or
[open it in Chibi Studio](https://waldnercharles.github.io/chibi-celeste/dev/).
Adding `?dev` to the player URL also opens the editor.

The editor starts from the published source snapshot. Browser edits stay in this
browser's local storage; export a project ZIP from Studio to keep a separate copy.
A new published source revision opens a new workspace and preserves earlier edits.

The Web workflow exports game content with published engine tools and copies a
published Studio bundle into `/dev/`. It publishes main automatically; pull requests
produce a downloadable site artifact. Neither path recompiles the engine or editor.
