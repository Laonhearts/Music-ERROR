from music21 import stream, note, meter, tempo, clef, instrument
from reportlab.pdfgen import canvas

# Create a music stream for the tenor trombone
score = stream.Score()
part = stream.Part()
part.insert(0, instrument.Trombone())
part.insert(0, clef.BassClef())
part.insert(0, meter.TimeSignature('4/4'))
part.insert(0, tempo.MetronomeMark(number=120))  # Set a moderate tempo

# Generate 16 measures of music with a "fireworks" feel using energetic rhythmic patterns
notes_sequence = [
    'C4', 'E4', 'G4', 'B4', 'D5', 'G4', 'C5', 'A4',  # Ascending pattern
    'G4', 'E4', 'C4', 'D4', 'B3', 'G3', 'F4', 'E4',  # Descending pattern
]

# Create measures and add notes to each measure
for i in range(16):
    measure = stream.Measure(number=i + 1)
    for pitch in notes_sequence:
        n = note.Note(pitch)
        n.quarterLength = 0.5  # Eighth notes for a lively feel
        measure.append(n)
    part.append(measure)

# Add the part to the score
score.append(part)

# Save the score as a PDF using reportlab
pdf_file_path = 'Tenor_Trombone_Fireworks_Score.pdf'
c = canvas.Canvas(pdf_file_path)

# Set the title and font for the PDF
c.setTitle("Tenor Trombone Fireworks Score")
c.setFont("Helvetica", 12)

# Write the score information to the PDF
text = c.beginText(40, 800)
text.textLine("Tenor Trombone Fireworks Score")
text.textLine("Time Signature: 4/4")
text.textLine("Tempo: 120 BPM")
text.textLine("Instrument: Tenor Trombone")
text.textLine(" ")

# Add the measures and notes to the PDF
for measure in part.getElementsByClass(stream.Measure):
    text.textLine(f"Measure {measure.number}:")
    for n in measure.notes:
        text.textLine(f"   Note: {n.nameWithOctave} - Duration: {n.quarterLength}")
    text.textLine(" ")

# Draw the text onto the PDF
c.drawText(text)

# Save the PDF file
c.save()

print(f"PDF file saved as: {pdf_file_path}")
