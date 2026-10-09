# Celeste Movement

Madeline's movement from Celeste, ported to Chibi script. Everything game-specific lives in
`content/`: the engine supplies only input, transforms and shapes.

- `behaviors/Player.chibi` ports the Normal, Climb and Dash states from
  [NoelFB/Celeste `Player.cs`](https://github.com/NoelFB/Celeste/blob/master/Source/Player/Player.cs):
  run, variable jump, coyote time, jump/dash buffering, wall slide, wall jump, climb, climb hop,
  stamina, 8-way dash with freeze frames, super, hyper and wall-bounce jumps, corner correction and
  ducking. It also simulates Madeline's hair (after `PlayerHair`), which turns blue with no dash left.
- `behaviors/CameraFollow.chibi` eases the camera toward the player inside the room bounds.
- `libraries/Room.chibi` is the 64x23 test room, generated from an ASCII map.

## Controls

| Action | Keyboard | Gamepad |
|---|---|---|
| Move | WASD | Left stick |
| Jump | Space or C | A |
| Dash | X or K | X |
| Grab | Z or L | Right shoulder |

Arrow keys are not movement sources in the engine yet.

## Art

Shapes only for now: Celeste's sprites are not openly licensed. Candidate CC0 packs, if sprites are added:

- [Kenney Pixel Platformer](https://kenney.nl/assets/pixel-platformer) - CC0
- [Pixel Frog, Pixel Adventure 1](https://pixelfrog-assets.itch.io/pixel-adventure-1) - CC0

No third-party asset is included in this project.
