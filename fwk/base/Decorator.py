import inspect, itertools

def aaa():
    pass

def handle_action(method):
    def wrapper(*args, **kwargs):
        # method_var_len = method.func_code.co_varnames.__len__()
        # if method_var_len == args.__len__():
        #     element_name = args[-1]
        #     idx_or_match = args[-2]
        # elif method_var_len - 1 == args.__len__():
        #     idx_or_match = args[-1]
        # python 3
        # bound_args = inspect.signature(method).bind(*args, **kwargs)
        # bound_args.apply_defaults()
        # print(dict(bound_args.arguments))
        try:
            args_dict = dict(itertools.izip(method.func_code.co_varnames, args), **dict(kwargs.iteritems()))
            self = args_dict.get("self")
            element_name = args_dict.get("element_name")
            idx_or_match = args_dict.get("idx_or_match")
            self._set_action_element(idx_or_match, element_name)
        except Exception as e:
            self.logger.error(e)
            raise Exception(e)
        try:
            method(*args, **kwargs)
        except Exception as e:
            self.logger.error(e)
            raise Exception("This action [{}] failed.".format(method.func_name))
        return self
    return wrapper
