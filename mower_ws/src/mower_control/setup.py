from setuptools import setup

package_name = 'mower_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Autonomous mower control nodes',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'mower_controller = mower_control.mower_controller:main',
        ],
    },
)
