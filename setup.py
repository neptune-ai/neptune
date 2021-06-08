from setuptools import setup


def main():
    setup(
        name='neptune',
        python_requires='>=3.6.0',
        version='0.0.0',
        description='Wrapper for Neptune client',
        author='neptune.ai',
        author_email='contact@neptune.ai',
        url='https://neptune.ai/',
        project_urls={
            'Tracker': 'https://github.com/neptune-ai/neptune-client/issues',
            'Source': 'https://github.com/neptune-ai/neptune-client',
            'Documentation': 'https://docs.neptune.ai/',
        },
        long_description='Neptune Client',
        license='Apache License 2.0',
        install_requires=['neptune-client'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: Apache Software License',
            'Natural Language :: English',
            'Operating System :: MacOS',
            'Operating System :: Microsoft :: Windows',
            'Operating System :: POSIX',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Programming Language :: Python :: Implementation :: CPython',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
        ],
        keywords=['MLOps', 'ML Experiment Tracking', 'ML Model Registry', 'ML Model Store', 'ML Metadata Store'],
    )


if __name__ == "__main__":
    main()
