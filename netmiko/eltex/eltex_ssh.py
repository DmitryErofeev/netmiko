import time
from netmiko.cisco_base_connection import CiscoSSHConnection


class EltexSSH(CiscoSSHConnection):
    def session_preparation(self):
        """Prepare the session after the connection has been established."""
        self.ansi_escape_codes = True
        self._test_channel_read()
        self.set_base_prompt()
        self.disable_paging(command="terminal datadump")

        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def enable(self, *args, **kwargs):
        """No implemented enable mode"""
        return ""

    def save_config(self, cmd="write", confirm=True, confirm_response="y"):
        """Saves Config."""
        return super().save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )
