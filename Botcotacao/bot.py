"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""


# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.FIREFOX

    # Uncomment to set the WebDriver path
    bot.driver_path = r"resources\geckodriver.exe"

    # Opens the BotCity website.
    bot.browse("https://www.google.com/search?q=dolar+hoje&sca_esv=e4b6c45cd17b4d13&sca_upv=1&source=hp&ei=fhJ5ZpTOJOzR1sQPsOaJ4As&iflsig=AL9hbdgAAAAAZnkgjqeAENdlio-HRsDVE9jFi8mE_WU7&oq=dola&gs_lp=Egdnd3Mtd2l6IgRkb2xhKgIIADINEAAYgAQYsQMYRhiCAjILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMgsQABiABBixAxiDATIIEAAYgAQYsQMyCBAAGIAEGLEDMgsQABiABBixAxiDATIIEAAYgAQYsQMyCBAAGIAEGLEDMggQABiABBixA0jL0gVQgLoFWL-_BXADeACQAQCYAakBoAGOBaoBAzAuNLgBA8gBAPgBAZgCB6ACtgWoAgrCAhAQABgDGOUCGOoCGIwDGI8BwgIQEC4YAxjlAhjqAhiMAxiPAcICDhAuGIAEGLEDGIMBGIoFwgIFEAAYgATCAg4QLhiABBixAxjRAxjHAcICERAuGIAEGLEDGNEDGIMBGMcBmAMGkgcDMy40oAfBHg&sclient=gws-wiz") 
    
    #input()
    
    if not bot.find("ancora-dolar", matching=0.97, waiting_time=10000):
        not_found("ancora-dolar")
    bot.click_relative(40, 50)
    
    
    bot.mouse_down()
    bot.move_relative(-100, 0)
    bot.mouse_up()
    
    # Coletando o valor do clipboard
    bot.control_c()
    valor_cotacao = bot.get_clipboard()
    print(f"Dólar => R$ {valor_cotacao}")
    
    

    # Implement here your logic...
    ...

    # Wait 3 seconds before closing
    bot.wait(3000)

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
