
API Documentation
=================

.. automodule:: penman

   .. contents:: Contents
      :local:

   Graphs and Triples
   ------------------

   .. autoclass:: Graph
      :members:

   .. autoclass:: Triple
      :members:

   Codec Classes
   -------------

   .. autoclass:: PENMANCodec
      :members:

   .. autoclass:: AMRCodec
      :show-inheritance:
      :members:

   Serialization Functions
   -----------------------

   .. autofunction:: decode
   .. autofunction:: encode
   .. autofunction:: load
   .. autofunction:: loads
   .. autofunction:: dump
   .. autofunction:: dumps

   Triple Sorting Functions
   ------------------------

   The :func:`original_order`, :func:`out_first_order`, and
   :func:`alphanum_order` functions are used during serialization to
   sort the relations on a node. By default, the observed order during
   decoding or graph construction is used, but if a particular order
   is to be used an appropriate function may be passed as the
   `relation_sort` parameter to a `PENMANCodec` instantiation.

   .. autofunction:: original_order
   .. autofunction:: out_first_order
   .. autofunction:: alphanum_order

   Exceptions
   ----------

   .. autoexception:: PenmanError

   .. autoexception:: EncodeError
      :show-inheritance:

   .. autoexception:: DecodeError
      :show-inheritance:
