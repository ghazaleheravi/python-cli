# import typer
# from typing import Annotated

# def greet(
#   name: Annotated[str, typer.Argument(help="The (last, if --title is given) name of the person to greet")] = "",
#   title: Annotated[str, type.Option(help="The prefered title of the person to greet")] = "",
#   count: Annotated[int, typer.Option(help="Number of times to greet the person")] = 1,
# ):
#   greeting = "Greetings, "
#   if not name:
#     if title:
#       name = title.lower().rstrip(".")
#     else:
#       name = "friend"
#   if title:
#     greeting += f"{title} "
#   greeting += f"{name}!"
#   for i in range(0, count):
#     print(greeting)

  
