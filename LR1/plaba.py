import click
import world as w

@click.command()
@click.option("--add", type=str)
@click.option("-x", type=int)
@click.option("-y", type=int)
@click.option("-l", "--lives", type=str)
@click.option("-sd", "--starve_days", type=str)
@click.option("-s", "--sex", type=str)
@click.option("--auto", type=int, help="N days pass")
@click.option("--next", "n", is_flag=True, help="One day passes")
@click.option("--info", "inf", is_flag=True, help="Prints iformation about the world")
def live(add, x, y, lives, starve_days, sex, auto, n, inf):
    World = w.world('info.txt')
    if add:
        x1, y1, l, sd, s = -1, -1, '', '0', ''
        if x:
            x1 = x
        if y:
            y1 = y
        if lives:
            l = lives
        if starve_days:
            sd = starve_days
        if sex:
            s = sex
        World.add(add,x=x1,y=y1,l=l,sd=sd,s=s)
    if auto:
        for i in range(auto):
            World.next()
    if n:
        World.next()
    if inf:
        World.show_info()
        
if __name__=='__main__':
    live()
