#Author: Vodohleb04

def after_done_emitter(emitter_signal):
    def emitter_wrapper(wrapped_function):
        def emitter(*args, **kwargs):
            wrapped_function_result = wrapped_function(*args, **kwargs)
            emitter_signal.emit()
            return wrapped_function_result
        return emitter
    return emitter_wrapper


def before_done_emitter(emitter_signal):
    def emitter_wrapper(wrapped_function):
        def emitter(*args, **kwargs):
            emitter_signal.emit()
            wrapped_function_result = wrapped_function(*args, **kwargs)
            return wrapped_function_result
        return emitter
    return emitter_wrapper
