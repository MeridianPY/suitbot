def arg_parse(ctx):
    args = ctx.message.content.split()[1:]
    for index, arg in enumerate(args):
        if len(arg) < 2:
            args[index - 1:index + 1] = [' '.join(args[index - 1:index + 1])]
    return args
