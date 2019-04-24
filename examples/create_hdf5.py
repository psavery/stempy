import click
import sys

from stempy import io, image

@click.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True, dir_okay=False))
@click.option('-r', '--rows', default=160, help='Number of rows')
@click.option('-c', '--columns', default=160, help='Number of columns')
@click.option('-i', '--inner-radius', default=40, help='Mask inner radius')
@click.option('-u', '--outer-radius', default=288, help='Mask outer radius')
@click.option('-o', '--output', default='stem_image.h5', help='Output file')
def make_stem_hdf5(files, rows, columns, inner_radius, outer_radius, output):
    """Make an HDF5 file containing a STEM image

    Example: "python create_hdf5.py /path/to/data/data*.dat"

    """

    if len(files) == 0:
        sys.exit('No files found')

    reader = io.reader(files)
    img = image.create_stem_image(reader, rows, columns, inner_radius,
                                  outer_radius);

    io.save_stem_image(output, img)

if __name__ == '__main__':
    make_stem_hdf5()
