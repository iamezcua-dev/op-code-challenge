class Utils:
    @staticmethod
    def normalize_line(line: str):
        """
        :param line: string containing one line of text
        :return: normalized_line (string) with leading/trailing spaces removed and converted to lowercase
        """
        normalized_line = line.lower().strip()  # delete leading/trailing spaces and lower
        return normalized_line
