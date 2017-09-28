import inspect
def handle_action(method):
    def wrapper(*args, **kwargs):
        dict_args = {}
        i = 0  # 0 is self
        for arg_name in method.func_code.co_varnames:
            try:
                dict_args[arg_name] = args[i]
            except:
                dict_args[arg_name] = None
            i += 1
        # python 3
        # bound_args = inspect.signature(method).bind(*args, **kwargs)
        # bound_args.apply_defaults()
        # print(dict(bound_args.arguments))

        try:
            element_name = dict_args["self"]._getCurrentElementNameWhenNone(dict_args["element_name"])
            element = dict_args["self"]._getCurrentElementObjectOrSearch(dict_args["idx_or_match"], dict_args["element_name"])
            dict_args["self"].logger.info("Click element [" + element_name + "] on the screen [" + str(dict_args["self"].getCurrentPageName()) + "].")
            return method(dict_args["self"], dict_args["idx_or_match"], dict_args["element_name"])
        except Exception as e:
            dict_args["self"].logger.error(e.__str__())
            dict_args["self"].logger.error("Failed to click element [" + element_name + "] on the screen [" + str(dict_args["self"].getCurrentPageName()) + "].")
            raise Exception("Failed to click element [" + element_name + "] on the screen [" + str(dict_args["self"].getCurrentPageName()) + "].")
        return self
    return wrapper
