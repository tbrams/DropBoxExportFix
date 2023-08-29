  README.md 
# Export all your DropBox Paper documents including images as Markdown
DropBox Paper has served me well for years now, but recently I have started experimenting with various locally hosted [Markdown](https://www.markdownguide.org/getting-started/) solutions that suited my workflow better and did not require a very expensive subscription.

## DropBox Image/screenshot issue
You can easily export DropBox Paper notes as Markdown, but unfortunately there is no way easy way to avoid DropBox hosting all images and screenshots in these files.

# Example
Having a lot of notes from back when I studied for the ATPL exam, I considered maintaining a locally hosted version of these instead of continuing the relatively expensive subscription just to these notes.

Exporting notes in Markdown format from Dropbox worked flawlessly. The Markdown rendered just as expected, but When I looked in the Markdown code, I noticed that all screenshots and images were still hosted by DropBox.

```Markdown
The radio bearing (relative bearing) of the NDB is measured inside the aircraft, so all corrections are applied at the aircraft estimated DR position. First the relative bearing is converted into a great circle bearing. Then it is converted into a rhumb line bearing. As the bearing is the bearing of the station from the aircraft, it must be converted info the bearing of he station from the aircraft, it must be converted into the ;bearing of the aircraft from the station (reciprocal) before it can be plotted.

- 030 RB + 048 TH = 078 TB (GC)
- 078 TB (GC) - 6 CA = 072 TB (RH line)
- 0 072 TB (RH line) + 180 - 252 TB (RL)

Calculate the difference between the directions of the Rhumb line and the Great Circle connecting the stations A (030N 045E) and B (030N 065E)  

$$Convergency = Dlong \cdot \sin(lat)$$
$$Dlong = 20$$

convergency = 10 and conversion angle =5  

![GC tracks are closer to the Poles]
(https://paper-attachments.dropbox.com/s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560581900134_image.png)

![]
(https://paper-attachments.dropbox.com/s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560581785324_image.png)

The RL direction is therefore 090 from the meridian and because the great circle should be closer to the pole, we can subtract the CA in the beginning and add it at the end of this line.

## Lambert’s conformal Chart

```

# What is this
This is a simple Python script that will run through all the markdown files in the current directory, download all referenced images and update the markdown code to use the local copy instead.

# Instructions
## 1. Export from DropBox
Make sure you select the "Markdown" format when downloading the selected papers to a local folder.  

## 2. Check downloads
I had to revisit the export page again and manually perform additional downloads to make sure I got all of my content from DropBox.
## 3. Fetch all images and update Markdown
When you have made sure you have all the desired files safely downloaded from DropBox, run this script in the directory containing your markdown files.

Run the script in the directory containing your markdown files and subdirectories. It will recursively search for all markdown files, download all the images from the links in each markdown file, save them in a subdirectory called "images" in the same directory as the markdown file, replace the links in the content with the local path to the images, and save the modified content to a new file with a "\_new" suffix in the filename.

## Updated Markdown example
```Markdown
...

The radio bearing (relative bearing) of the NDB is measured inside the aircraft, so all corrections are applied at the aircraft estimated DR position. First the relative bearing is converted into a great circle bearing. Then it is converted into a rhumb line bearing. As the bearing is the bearing of the station from the aircraft, it must be converted info the bearing of he station from the aircraft, it must be converted into the ;bearing of the aircraft from the station (reciprocal) before it can be plotted.

- 030 RB + 048 TH = 078 TB (GC)
- 078 TB (GC) - 6 CA = 072 TB (RH line)
- 0 072 TB (RH line) + 180 - 252 TB (RL)

Calculate the difference between the directions of the Rhumb line and the Great Circle connecting the stations A (030N 045E) and B (030N 065E)

$$Convergency = Dlong \cdot \sin(lat)$$
$$Dlong = 20$$

convergency = 10 and conversion angle =5

![GC tracks are closer to the Poles]
(images/s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560581900134_image.png)

![] (images/s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560581785324_image.png)  

The RL direction is therefore 090 from the meridian and because the great circle should be closer to the pole, we can subtract the CA in the beginning and add it at the end of this line.
  
## Lambert’s conformal Chart

...
```


## Terminal Session example
```bash
ATPL % python3 fetchAndFixImages.py
  
Saved modified content to Airlaw_Notes_new.md

...

Downloaded s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560771487601_image.png

Downloaded s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560771535371_image.png

Downloaded s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560771583085_image.png

Downloaded s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560771683043_image.png

Downloaded s_70815E4BE57C42BF26C8ACC2D279D3BC59CE7EC307A33D1E339437C0C5822362_1560800737076_image.png

Saved modified content to GNAV_Notes_new.md

...

Process completed
```

## Preview example
![](images/Screenshot%202023-08-29%20at%2010.22.14.png)
