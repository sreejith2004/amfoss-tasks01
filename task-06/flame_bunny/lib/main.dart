import 'package:flutter/material.dart';
import 'package:flame/game.dart';
import 'package:flame/components.dart';
import 'package:flutter/cupertino.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(Application());
}

class Application extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: GameScreen(),
    );
  }
}

class GameScreen extends StatelessWidget {
  final MyGame game = MyGame();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Bunny_Game created by Sreejith')),
      body: Stack(
        children: [
          GameWidget(game: game),
          ControlPanel(game: game),
        ],
      ),
    );
  }
}

class MyGame extends FlameGame {
  SpriteComponent bunny = SpriteComponent();
  SpriteComponent background = SpriteComponent();

  bool moveLeft = false;
  bool moveRight = false;
  bool moveUp = false;
  bool moveDown = false;

  @override
  Future<void> onLoad() async {
    super.onLoad();
    print('Loading game assets');

    // Load background
    add(background
      ..sprite = await loadSprite('background.png')
      ..size = size);

    // Load bunny
    bunny
      ..sprite = await loadSprite('bunny.png')
      ..size = Vector2(100, 100)
      ..y = 100;
    add(bunny);
  }

  void updateBunny(double dt) {
    if (moveLeft) {
      bunny.x -= 30 * dt;
    }
    if (moveRight) {
      bunny.x += 30 * dt;
    }
    if (moveUp) {
      bunny.y -= 30 * dt;
    }
    if (moveDown) {
      bunny.y += 30 * dt;
    }
  }

  @override
  void update(double dt) {
    super.update(dt);
    updateBunny(dt);
  }
}

class ControlPanel extends StatefulWidget {
  final MyGame game;

  ControlPanel({required this.game});

  @override
  _ControlPanelState createState() => _ControlPanelState();
}

class _ControlPanelState extends State<ControlPanel> {
  bool isEnabled = true;

  @override
  Widget build(BuildContext context) {
    return Positioned(
      top: 90,
      left: 0,
      child: Container(
        color: Colors.transparent,
        width: 170,
        height: 250,
        child: Center(
          child: Stack(
            children: <Widget>[
              // ...
              GestureDetector(
                  onTapDown: (_) {
                    setState(() {
                      widget.game.moveLeft = true;
                      widget.game.moveRight = false;
                      widget.game.moveUp = false;
                      widget.game.moveDown = false;
                    });
                  },
                  onTapUp: (_) {
                    setState(() {
                      widget.game.moveLeft = false;
                    });
                  },
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white70,
                      borderRadius: BorderRadius.circular(25),
                    ),
                    margin: EdgeInsets.only(left: 0, top: 150),
                    child: Center(
                      child: IconButton(
                        icon: Icon(
                          Icons.keyboard_arrow_left_rounded,
                          color: Colors.black,
                          size: 50,
                        ),
                        onPressed: () {
                          // Add onPressed callback function here
                        },
                        padding:
                            EdgeInsets.symmetric(vertical: 0, horizontal: 0),
                      ),
                    ),
                  )),
              GestureDetector(
                  onTapDown: (_) {
                    setState(() {
                      widget.game.moveUp = true;
                      widget.game.moveLeft = false;
                      widget.game.moveRight = false;
                      widget.game.moveDown = false;
                    });
                  },
                  onTapUp: (_) {
                    setState(() {
                      widget.game.moveUp = false;
                    });
                  },
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white70,
                      borderRadius: BorderRadius.circular(25),
                    ),
                    margin: EdgeInsets.only(left: 45, top: 100),
                    child: Center(
                      child: IconButton(
                        icon: Icon(
                          Icons.keyboard_arrow_up_rounded,
                          color: Colors.black,
                          size: 50,
                        ),
                        onPressed: () {
                          // Add onPressed callback function here
                        },
                        padding:
                            EdgeInsets.symmetric(vertical: 0, horizontal: 0),
                      ),
                    ),
                  )),
              GestureDetector(
                  onTapDown: (_) {
                    setState(() {
                      widget.game.moveDown = true;
                      widget.game.moveLeft = false;
                      widget.game.moveRight = false;
                      widget.game.moveUp = false;
                    });
                  },
                  onTapUp: (_) {
                    setState(() {
                      widget.game.moveDown = false;
                    });
                  },
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white70,
                      borderRadius: BorderRadius.circular(25),
                    ),
                    margin: EdgeInsets.only(left: 45, top: 195),
                    child: Center(
                      child: IconButton(
                        icon: Icon(
                          Icons.keyboard_arrow_down_rounded,
                          color: Colors.black,
                          size: 50,
                        ),
                        onPressed: () {
                          // Add onPressed callback function here
                        },
                        padding:
                            EdgeInsets.symmetric(vertical: 0, horizontal: 0),
                      ),
                    ),
                  )),
              GestureDetector(
                  onTapDown: (_) {
                    setState(() {
                      widget.game.moveRight = true;
                      widget.game.moveLeft = false;
                      widget.game.moveUp = false;
                      widget.game.moveDown = false;
                    });
                  },
                  onTapUp: (_) {
                    setState(() {
                      widget.game.moveRight = false;
                    });
                  },
                  child: Container(
                    width: 50,
                    height: 50,
                    decoration: BoxDecoration(
                      color: Colors.white70,
                      borderRadius: BorderRadius.circular(25),
                    ),
                    margin: EdgeInsets.only(left: 90, top: 150),
                    child: Center(
                      child: IconButton(
                        icon: Icon(
                          Icons.keyboard_arrow_right_rounded,
                          color: Colors.black,
                          size: 50,
                        ),
                        onPressed: () {
                          // Add onPressed callback function here
                        },
                        padding:
                            EdgeInsets.symmetric(vertical: 0, horizontal: 0),
                      ),
                    ),
                  )),
            ],
          ),
        ),
      ),
    );
  }
}
