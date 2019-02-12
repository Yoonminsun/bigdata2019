import game.sound.echo
# from game.sound.echo import echo_test
# from game.sound.echo import * # sound에 __init__.py 생성 후 __all__ = ['echo'] (package)

imvari = game.sound.echo # 지역변수로 대입하여 사용할 수 있다
imvari.echo_test()
# game.sound.echo.echo_test()
# echo_test()
# render_test()