from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import box
import requests
import pyttsx3
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

console = Console()
city = input("🌍 Enter city name: ").strip()

# --- Fetch weather data
try:
    response = requests.get(f"https://wttr.in/{city}?format=j1", timeout=5)
    response.raise_for_status()
    data = response.json()
except (requests.RequestException, ValueError):
    print("[bold red]⚠️ Error fetching weather data. Check city name or connection.[/]")
    exit()

# --- Extract values
current = data['current_condition'][0]
temp = int(current['temp_C'])
feels_like = int(current['FeelsLikeC'])
humidity = int(current['humidity'])
wind_kph = int(current['windspeedKmph'])
uv = int(current['uvIndex'])
desc = current['weatherDesc'][0]['value']


# --- Helper functions
def color_temp(t):
    if t <= 0:
        return f"[blue]{t}°C[/]"
    elif t < 20:
        return f"[cyan]{t}°C[/]"
    elif t < 30:
        return f"[orange1]{t}°C[/]"
    else:
        return f"[red]{t}°C[/]"


def wind_color(w):
    if w < 10:
        return f"[green]{w} km/h[/]"
    elif w < 30:
        return f"[yellow]{w} km/h[/]"
    else:
        return f"[red]{w} km/h[/]"


def uv_warning(uv):
    if uv <= 2:
        return f"[green]{uv} (low)[/]"
    elif uv <= 5:
        return f"[yellow]{uv} (moderate)[/]"
    elif uv <= 7:
        return f"[orange1]{uv} (high)[/]"
    else:
        return f"[red]{uv} (very high)[/]"


# --- Display in rich table
table = Table(title=f"🌤️ [bold cyan]Weather in {city.capitalize()}[/]",
              header_style="bold white",
              box=box.SQUARE,
              show_lines=True,
              border_style="cyan")

table.add_column("📌 Parameter", justify="center", style="bold")
table.add_column("📊 Value", justify="center")

table.add_row("📝 Description", f"[italic magenta]{desc}[/]")
table.add_row("🌡 Temperature", f"{color_temp(temp)} (feels like {color_temp(feels_like)})")
table.add_row("💧 Humidity", f"[blue]{humidity}%[/]")
table.add_row("🌬 Wind", wind_color(wind_kph))
table.add_row("🔆 UV Index", uv_warning(uv))

console.print(table)

console.print(Panel.fit("[bold green]Have a great day![/] 🐍",
                        title="☀️ [cyan]Forecast complete[/]",
                        border_style="bright_magenta"))

# --- Text-to-Speech
tts = pyttsx3.init()
speech = f"Weather in {city}. {desc}. Temperature {temp} degrees Celsius, feels like {feels_like}. Humidity {humidity} percent. Wind {wind_kph} kilometers per hour. UV index {uv}."
tts.say(speech)
tts.runAndWait()

# --- Generate PDF
pdf_file = f"forecast_{city.lower()}.pdf"
c = canvas.Canvas(pdf_file, pagesize=A4)
text = c.beginText(50, 800)
text.setFont("Helvetica", 14)

text.textLine(f"Weather Forecast for {city.capitalize()}")
text.textLine("")
text.textLine(f"Description: {desc}")
text.textLine(f"Temperature: {temp}°C (feels like {feels_like}°C)")
text.textLine(f"Humidity: {humidity}%")
text.textLine(f"Wind: {wind_kph} km/h")
text.textLine(f"UV Index: {uv}")
text.textLine("")
text.textLine("Powered by wttr.in")

c.drawText(text)
c.showPage()
c.save()

print(f"[bold cyan]📄 PDF file generated: [green]{pdf_file}[/]")
