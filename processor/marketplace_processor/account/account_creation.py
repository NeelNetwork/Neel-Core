# Copyright 2017 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------

from sawtooth_sdk.processor.exceptions import InvalidTransaction


def handle_account_creation(create_account, header, state):
    """Handles creating an Account.

    Args:
        create_account (CreateAccount): The transaction.
        header (TransactionHeader): The header of the Transaction.
        state (MarketplaceState): The wrapper around the Context.

    Raises:
        InvalidTransaction
            - The public key already exists for an Account.
    """

    if state.get_account(public_key=header.signer_public_key):
        raise InvalidTransaction("Account with public key {} already "
                                 "exists".format(header.signer_public_key))

    state.set_account(
        public_key=header.signer_public_key,
        label=create_account.label,
        description=create_account.description,
        holdings=[])


# SmallBank send payment 
def handle_send_payment(send_payment, header, state):

    if state.get_account(public_key=header.signer_public_key):
        raise InvalidTransaction("Account with public key {} already "
                                 "exists".format(header.signer_public_key))

    
    #TODO add try catch
    source_account = header.signer_public_key

    dest_account = send_payment.dest_customer_id

    if source_account and dest_account :
        raise InvalidTransaction("Both source and dest accounts must exist")

    return "success!!!"
    #TODO
    # if source_account.CheckingBalance < sendPaymentData.Amount {
    #     return &processor.InvalidTransactionError{Msg: "Insufficient funds in source checking account"}
    # }

    # new_source_account := &smallbank_pb2.Account{
    #     CustomerId:      source_account.CustomerId,
    #     CustomerName:    source_account.CustomerName,
    #     SavingsBalance:  source_account.SavingsBalance,
    #     CheckingBalance: source_account.CheckingBalance - sendPaymentData.Amount,
    # }

    # new_dest_account := &smallbank_pb2.Account{
    #     CustomerId:      dest_account.CustomerId,
    #     CustomerName:    dest_account.CustomerName,
    #     SavingsBalance:  dest_account.SavingsBalance,
    #     CheckingBalance: dest_account.CheckingBalance + sendPaymentData.Amount,
    # }

    # saveAccount(new_source_account, context)
    # saveAccount(new_dest_account, context)
