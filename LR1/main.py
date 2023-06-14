import com
import roads


def work():
    railroad = [roads.RailR([], {}, [])]
    while True:
        session_ended = com.get_command(railroad)
        if session_ended:
            break


work()
