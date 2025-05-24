


from textual.app import App
from textual.app import ComposeResult
from textual.containers import ScrollableContainer
from textual.containers import Vertical
from textual.events import Key
from textual.widgets import Input
from textual.widgets import Static



AINSWER = (
    'Lorem ipsum dolor sit amet, '
    'consectetur adipiscing elit. ')



class ChatCLI(App):


    CSS = (
        """
        #history {
          background: #071A1A;
          border: solid #66FFFF;
          height: 1fr;
          margin: 0 1 0 1;
          overflow-y: auto;
          scrollbar-color: #0F6868;
          scrollbar-color-active: #66FFFF;
          scrollbar-color-hover: #09CDCD;
          scrollbar-corner-color: #0F6868; }

        #history Static {
          padding: 1 2 1 2; }

        #history Static:odd {
          background: #0A3232; }

        #input {
          background: #071A1A;
          border: solid #66FFFF;
          height: 3;
          margin: 0 1 0 1;
          padding: 0 0 0 1; }

        Toast {
          background: #0F6868;
          border-left: solid #66FFFF; }

        Toast.-information {
          border-left: solid #66DDFF; }

        Toast.-warning {
          border-left: solid #FFFF66; }

        Toast.-error {
          border-left: solid #FF6666; }
        """)


    def compose(
        self,
    ) -> ComposeResult:

        with Vertical():

            yield ScrollableContainer(
                id='history')

            yield Input(
                id='input',
                placeholder='Message')


    def on_mount(
        self,
    ) -> None:

        query = self.query_one

        query('#input').focus()


    def on_key(
        self,
        event: Key,
    ) -> None:

        if event.key == 'ctrl+d':
            self.exit()


    async def on_input_submitted(
        self,
        event: Input.Submitted,
    ) -> None:

        value = event.value
        query = self.query_one

        if not value.strip():
            return self.notify(
                'No input provided',
                severity='error')

        history = query('#history')

        message = Static(
            '[bold #66FFFF]'
            f'> [/]{value}')

        ainswer = Static(
            f'{AINSWER * 80}')

        history.mount(message)
        history.mount(ainswer)
        history.scroll_end()
        event.input.clear()



if __name__ == '__main__':
    ChatCLI().run()
