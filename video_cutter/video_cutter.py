import imageio

def clip_video(filename, output, start, end):
	in_vid = imageio.get_reader(filename, 'ffmpeg')

	# not supported for version v2.1.2
	# out_vid = imageio.get_writer(output)
	# out_vid.set_meta_data(in_vid.get_meta_data())
	# instead we copy the fps only
	fps = in_vid.get_meta_data()['fps']
	out_vid = imageio.get_writer(output, 'ffmpeg', fps=fps)

	# copy the frames over to out_vid
	for i in range(end):
		frame = in_vid.get_data(i)
		if(i<start):
			continue
		out_vid.append_data(frame, meta=frame.meta)

	in_vid.close()
	out_vid.close()
	del in_vid
	del out_vid

clip_video('video.mp4', 'output.mp4', 100, 5000)

# Display image
# import pylab
# fig = pylab.figure()
# image = in_vid.get_data(index)
# fig.suptitle('image #{}'.format(index), fontsize=20)
# pylab.imshow(image)
# pylab.show()