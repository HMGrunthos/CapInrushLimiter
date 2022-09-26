import pcbnew
board = pcbnew.GetBoard()

tracksegments = [t for t in board.GetTracks() if (t.GetClass() == 'PCB_TRACK' and t.IsSelected())]
for s in tracksegments:
	line = pcbnew.PCB_SHAPE(board)
	line.SetShape(pcbnew.S_SEGMENT)
	line.SetLayer(pcbnew.B_Mask)
	line.SetWidth(s.GetWidth() + 50000)
	line.SetEnd(s.GetEnd())
	line.SetStart(s.GetStart())
	board.Add(line)
	print("Added line\n")

tracksegments = [t for t in board.GetTracks() if (t.GetClass() == 'PCB_ARC' and t.IsSelected())]
for s in tracksegments:
	arc = pcbnew.PCB_SHAPE(board)
	arc.SetShape(pcbnew.S_ARC)
	arc.SetLayer(pcbnew.B_Mask)
	arc.SetWidth(s.GetWidth() + 50000)
	arc.SetArcGeometry(s.GetStart(), s.GetMid(), s.GetEnd())
	board.Add(arc)
	print("Added arc\n")

pcbnew.Refresh()
