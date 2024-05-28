from sketchpy import library
import turtle

def draw_rdj():
    obj = library.rdj()
    obj.draw()
    turtle.bye()

def draw_tom_holland():
    obj = library.tom_holland()
    obj.draw()
    turtle.bye()

def draw_ironman_ascii():
    obj = library.ironman_ascii()
    obj.draw()
    # Não é necessário fechar a janela da turtle para o desenho ASCII

if __name__ == "__main__":
    draw_rdj()
    draw_tom_holland()
    draw_ironman_ascii()
