from pyowm import OWM
import discord
from discord.ext import commands


# Basic weather cog i have written for my discord bot. Example use : (bot_prefix)weather istanbul


class weather():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def weather(self, ctx, *, city: str):
        """Returns available data for a given city"""
        
        # Enter Your Own Api key.Get one from openweather.org
        API_key = 'api key here'
        owm = OWM(API_key)
        server_embed = discord.Embed(color=10221224)
        obs = owm.weather_at_place(city)
        
        # Get some values from api
        w = obs.get_weather()
        l = obs.get_location()
        country = l.get_country()
        name = l.get_name()
        ids = l.get_ID()
        time = w.get_reference_time(timeformat='iso')
        cloud = w.get_clouds()
        rain = w.get_rain()
        det = w.get_detailed_status()
        snow = w.get_snow()
        wind = w.get_wind()['speed']
        hum = w.get_humidity()
        press = w.get_pressure()['press']
        tem = w.get_temperature(unit='celsius')['temp']
        status = w.get_status()
        icon = w.get_weather_icon_name()
        sunr = w.get_sunrise_time('iso')
        suns = w.get_sunset_time('iso')
        url2 = 'http://openweathermap.org/img/w/'+icon+'.png'
        link = 'http://openweathermap.org/city/'+str(ids)

        # Build the embed
        server_embed.set_author(name="Weather for this city",
                                icon_url='http://www.pvhc.net/img38/bxfljjwtbnrfmjjvjwiu.png')
        server_embed.add_field(name=":map: Location", value=name+','+country)
        server_embed.add_field(name=":cloud: Cloud Coverage", value=cloud)
        server_embed.add_field(name=":cloud_rain: Rain Volume", value=rain, inline=True)
        server_embed.add_field(name=":snowflake: Snow Volume", value=snow, inline=True)
        server_embed.add_field(name=":wind_blowing_face: Wind (m/s)", value=wind, inline=True)
        server_embed.add_field(name=":sweat_drops: Humidity (%)", value=hum, inline=True)
        server_embed.add_field(name=":sunny: Temperature (*C)", value=tem, inline=True)
        server_embed.add_field(name=":information_source: Status",
                               value=status+','+det, inline=True)
        server_embed.add_field(name=":sunrise: Sun Rise", value=sunr, inline=True)
        server_embed.add_field(name=":city_sunset: Sun Set", value=suns, inline=True)
        server_embed.add_field(name=":link: More info", value=link)
        server_embed.set_thumbnail(url=url2)
        server_embed.set_footer(text='Data From '+time)
        
        # Send The embed
        await self.bot.say(embed=server_embed)

# Define & Add it as cog
def setup(bot):
    bot.add_cog(weather(bot))
    print('weather is loaded')
