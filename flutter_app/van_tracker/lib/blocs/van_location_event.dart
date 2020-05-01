part of 'van_location.dart';

@immutable
abstract class VanLocationEvent extends Equatable {
  const CartEvent();
}

class LoadCart extends VanLocationEvent {
  @override
  List<Object> get props => [];
}

class AddItem extends VanLocationEvent {
  final Item item;

  const AddItem(this.item);

  @override
  List<Object> get props => [item];
}