import textwrap


class ErrorReporterMixin:
    @staticmethod
    def error_message(actual_status, expected_status, method, uri, payload, response_content, details=''):
        msg = f"""
        - Received: {actual_status}, Expected: {expected_status}
        - {method}: {uri}

        - payload: {payload}

        - response content: {response_content}

        """
        if details:
            msg += f"- details: {details}"
        return textwrap.dedent(msg)
