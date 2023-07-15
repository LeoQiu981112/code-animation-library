import webcolors


class ColorConverter:
    """
    Utility class for converting colors between various formats.
    """

    @staticmethod
    def convert_color(color: str, source_format: str, target_format: str) -> str:
        """
        Convert a color from one format to another.

        Args:
            color: The color to convert.
            source_format: The current format of the color.
            target_format: The format to convert the color to.

        Returns:
            The color in the target format.

        Raises:
            ValueError: If the source or target format is not supported.
        """
        if source_format == target_format:
            return color

        if source_format == "rgb":
            rgb_color = color
        elif source_format == "hex":
            rgb_color = webcolors.hex_to_rgb(color)
        elif source_format == "name":
            rgb_color = webcolors.name_to_rgb(color)
        else:
            raise ValueError(f"Unsupported source color format: {source_format}")

        if target_format == "rgb":
            return rgb_color
        elif target_format == "hex":
            hex_color = webcolors.rgb_to_hex(rgb_color, force_long=True)
            return hex_color
        elif target_format == "name":
            color_name = webcolors.rgb_to_name(rgb_color)
            return color_name
        else:
            raise ValueError(f"Unsupported target color format: {target_format}")
